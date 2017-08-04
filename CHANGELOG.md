# Change Log
All notable changes to this project will be documented in this file.

## [1.9.3] - 2017-08-04
### Added
- Adding 'chrome-headless' option.
- `-p, --processes` flag for webrunner. (Number of simultaneous browser instances)
- Add set_window_size method
- Add refresh method
- Add maximize_window method
- Add add_cookie method
- Add delete_cookie method
- Add delete_all_cookies method

### Changed
- Update Selenium requirement

## [1.9.2] - 2017-08-02
### Added
- Update Gecko
- Fix geckodriver download
- Try to fix Gecko on start.

## [1.9.1] - 2017-08-02
### Added
- download method
- save_image method

## [1.9.0] - 2016-12-20
### Added
- set_default_offset method
- `-do, --default-offset` parameters for webrunner
- default_offset parameter for scroll_to_element

## [1.8.9] - 2016-12-14
### Added
- chromedriver failure detection
- chromedriver latest version detection

### Changed
- Prompts to fix chromedriver installation if chromedriver crash.
- Updated wires to latest version 0.11.1

## [1.8.8] - 2016-09-16
### Changed
- Added `driver_init_timeout` parameter to control the timeout of instantiating the driver.

## [1.8.7] - 2016-09-16
### Changed
- Simplified `scroll_to_element` to accept offset parameters.

## [1.8.6] - 2016-09-16
### Added
- `-v, --verbose` flag for webrunner.
- `(( prompt|Something ))` parameter added.

## [1.8.5] - 2016-09-12
### Changed
- Better YAML script error handling.

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
