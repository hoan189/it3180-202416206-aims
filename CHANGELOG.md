# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added
- Add Cart.sort_by_title() to sort DVDs alphabetically by title.
- Add Cart.sort_by_cost() to sort DVDs by ascending cost.
- Add unit tests for cart sorting.

## [1.0.0] - 2026-11-07

### Added
- Add Cart.print_cart() to display cart contents.
- Add search_by_title() to search DVDs by title.
- Add total_cost_after_discount() to calculate discounted cart cost.
- Add Vietnamese messages when adding DVDs to the cart.
- Add unit tests for cart, discount and DVD search.

### Fixed
- Fix cart accepting the 21st DVD (#6).
- Handle empty cart when printing cart contents.