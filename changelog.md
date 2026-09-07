# Changelog

## 2.2.0 - 2026-09-07

_Build 42 support_

### Added

- Full support for the admin and RCON commands documented for Project Zomboid Build 42.20.2
- New command methods for key management, Steam ID allowlisting, IP bans, player-specific admin actions, Lua reloading, item removal, map symbol removal, password changes, and world generation
- Passthrough methods for Build 42 commands whose arguments are not yet documented by Project Zomboid
- Optional command-specific help with `help("command")`
- Optional kick reasons with `kickuser("user", reason="reason")`

### Changed

- Updated `addvehicle()` to support either a player name or coordinates as its target
- Updated `setaccesslevel()` documentation with the Build 42 access levels
- Updated the command reference and test coverage for Build 42

### Deprecated

- `replay()` was removed from Project Zomboid Build 42 and now emits a warning while remaining available for Build 41 servers
- `clear()` is no longer listed as a Build 42 command and now emits a warning while remaining available for Build 41 servers

## 2.1.0 - 2026-06-12

First contribution by [ashy-ls](https://github.com/ashy-ls)

### Added

- Ability to test that RCON connections are successful with pings in [#13](https://github.com/jmwhitworth/zomboid_rcon/pull/13)

## 2.0.0 - 2026-06-04

_Build 41 support_

### Added

- Missing build 41 commands, bringing us to full support for build 41
- Better exception handling
- Additional test coverage
- Support for Windows-based systems

### Removed

- `timeout_decorator` dependency, meaning Windows systems are now supported.

## 1.0.0 - 2023-07-23

_First full release_