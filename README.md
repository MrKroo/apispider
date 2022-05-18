apispider
=========

This script crawls the API of news.ycombinator.com and retrieve posts. Once the timeout is reached, it search through the file and get the URL from posts only if the score is higher than 100. Then, from the URL, it filters only if "github" is included.

I wrote this script so I can crawl through interesting news and gits.

Usage
-----

`./script TIME`

The value TIME in seconds is how much time the script should load from the most recent item to oldest. Default value is 3600.

This script is licensed with GNU General Public License v2.
