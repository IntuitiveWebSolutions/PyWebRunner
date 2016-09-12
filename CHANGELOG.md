# Change Log
All notable changes to this project will be documented in this file.

## [1.8.4] - 2016-09-12
### Added
- `set_timeout` command for altering the global wait timeout on the fly.
- `-t, --timeout` flag for webrunner

## [1.8.2] - 2016-09-12
### Added
- `focus_browser` command. Uses JS alert to focus the browser in the OS.
- `focus_window` command. Takes in an index of the window number to focus on.
- `--focus` option for webrunner to automatically run `focus_browser` on launch.

## [1.8.1] - 2016-09-08
### Added
- Automatically install "geckodriver" as well as "wires" for forward compat with Selenium 3X

### Changed
- Fix set_value on Nightly Firefox + Selenium 3 beta for Gecko
- Etc... Geckodriver is horrible right now.
- Default to Chrome.


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
