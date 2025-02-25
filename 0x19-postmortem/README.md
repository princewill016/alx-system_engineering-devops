# Postmortem: WordPress Application 500 Error Incident

## Issue Summary
**Duration**: October 10, 2024, 09:15 - 11:45 UTC  
**Impact**: The company WordPress application returned 500 errors to 100% of users attempting to access the site. Users were completely unable to view blog posts, comment, or interact with any site content.  
**Root Cause**: A typographical error in the WordPress configuration file (wp-settings.php) where a PHP extension was misspelled as "phpp" instead of "php", causing the server to fail when attempting to include required files.

## Timeline
* **09:15 UTC** - Issue began when a deployment containing the misconfiguration was pushed to production
* **09:22 UTC** - First monitoring alert triggered for increased 500 error rate
* **09:28 UTC** - On-call engineer acknowledged the alert and began investigation
* **09:35 UTC** - Initial focus on recent database changes based on assumption of data corruption
* **09:50 UTC** - Database investigation yielded no results; investigation pivoted to web server logs
* **10:05 UTC** - Apache error logs showed PHP errors but didn't provide clear indication of the source file
* **10:15 UTC** - Used `strace` to attach to the Apache process to trace system calls during request processing
* **10:27 UTC** - `strace` output revealed attempts to access non-existent ".phpp" files
* **10:33 UTC** - Searched codebase for ".phpp" references and found the typo in wp-settings.php
* **10:40 UTC** - Manually fixed the typo in wp-settings.php to verify the solution
* **10:45 UTC** - Confirmed the fix resolved the issue; site began responding normally
* **11:15 UTC** - Created Puppet manifest to automate the fix across all servers
* **11:45 UTC** - Fix deployed to all production servers; incident closed

## Root Cause and Resolution
The root cause was identified as a typographical error in the WordPress configuration file (wp-settings.php). During a recent code update, a developer accidentally wrote `require_once( ABSPATH . WPINC . '/class-wp-dependency.phpp' );` instead of the correct `require_once( ABSPATH . WPINC . '/class-wp-dependency.php' );`. When PHP attempted to include this file, it failed because no file with the ".phpp" extension existed, causing the application to crash and return 500 errors.

The issue was resolved by correcting the file extension from ".phpp" to ".php" in the wp-settings.php file. This was initially done manually to verify the fix, and then automated using a Puppet manifest to ensure consistency across all servers. The Puppet manifest used sed to find and replace all instances of ".phpp" with ".php" in the wp-settings.php file.

## Corrective and Preventative Measures
To prevent similar issues in the future, we've identified several improvement areas:

**General Improvements:**
- Enhance pre-deployment testing to catch configuration errors
- Implement stricter code review processes for configuration changes
- Add syntax validation checks for PHP files in the CI/CD pipeline
- Improve monitoring to detect and alert on PHP parsing errors specifically

**Specific Tasks:**
1. Create automated test to verify all required PHP files can be properly included
2. Implement PHP lint checks in the CI/CD pipeline for all PHP files
3. Add file extension validation script to pre-commit hooks
4. Set up monitoring for specific PHP include/require errors in Apache logs
5. Update deployment process to include a canary deployment step to catch errors before full rollout
6. Create documentation for using `strace` and other debugging tools for faster troubleshooting
7. Schedule training session for the development team on common configuration pitfalls
8. Add explicit validation of wp-settings.php during the deployment process
