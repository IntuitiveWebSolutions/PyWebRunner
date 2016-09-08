# Change Log
All notable changes to this project will be documented in this file.


## [1.8.1] - 2016-09-08
### Added
- Automatically install "geckodriver" as well as "wires" for forward compat with Selenium 3X

### Changed
- Fix set_value on Nightly Firefox + Selenium 3 beta for Gecko
- Etc... Geckodriver is horrible right now.


## [1.8.0] - 2016-09-07
### Added
- This CHANGELOG file
- Gecko driver option
- Timeout for driver load. (To detect Firefox 48+ no longer working with Selenium)
- Detect `wires` executable and default to Gecko by default if so.
- Command line option for `webrunner`: --browser
- Added `include` command for yaml scripts. Allows inclusion of other yaml scripts.
- Added `assert_element_count` to WebTester.
- Added helper wizard for installing geckodriver (wires) and chromedriver. Auto-prompts if either is needed.

### Changed
- Try/Except around the JSErrorCollector plugin load just in case.
