# Data Dictionary

This document describes the main fields used in the standardized datasets of Stable-Context: Brazil.

The data dictionary focuses on fields used across the Bronze, Silver and Gold layers.

## General Fields

| Field | Type | Description |
|---|---|---|
| `protocol` | string | DeFi protocol associated with the observation. |
| `market` | string | Unique identifier of the lending market. |
| `market_name` | string | Human-readable name of the market. |
| `asset` | string | Stablecoin associated with the market, such as USDC or USDT. |
| `token_address` | string | On-chain contract address of the input token. |
| `token_decimals` | integer | Number of decimal places defined by the token contract. |
| `timestamp` | integer | Unix timestamp associated with the daily observation. |

## Market Activity Fields

| Field | Type | Description |
|---|---|---|
| `input_token_balance` | float | Balance of the market's input token represented by the snapshot. |
| `input_token_price_usd` | float | USD price of the input token at the snapshot. |
| `total_value_locked_usd` | float | Total value locked in the market, expressed in USD. |
| `daily_deposit_usd` | float | Value of deposits recorded for the day, expressed in USD. |
| `daily_borrow_usd` | float | Value of borrowing activity recorded for the day, expressed in USD. |
| `daily_withdraw_usd` | float | Value of withdrawals recorded for the day, expressed in USD. |
| `daily_repay_usd` | float | Value of repayment activity recorded for the day, expressed in USD. |
| `daily_active_users` | integer | Number of users active in the market during the day according to the standardized dataset. |

## Derived Fields

Derived analytical fields may be introduced in the Gold layer.

They must be calculated from documented source fields and should not replace the underlying observations.

Examples may include:

- Monthly deposit volume
- Monthly borrow volume
- Monthly active users
- Changes in TVL
- Rolling averages
- Cross-protocol comparisons

Derived fields will be documented when they are introduced.

## Time Representation

The Silver layer stores timestamps as Unix timestamps.

For analysis and presentation, timestamps may be converted to calendar dates or periods such as:

- Day
- Month
- Quarter
- Year

The original timestamp remains the reference for reproducibility.

## Units

The project preserves the unit associated with each field.

- USD values are represented in US dollars.
- Token balances are represented in the token's native units after standardized decoding.
- Counts represent number of events or users according to the source definition.
- Timestamps are Unix timestamps in seconds.

## Source Semantics

Fields are interpreted according to the source that produced them.

A field with the same name across standardized datasets is treated as comparable only when the underlying schema and definition are equivalent.

Standardization improves comparability but does not eliminate differences in protocol behavior or data coverage.

## Missing and Zero Values

Missing values and zero values are not assumed to have the same meaning.

- A zero may represent an observed value of zero.
- A missing value may indicate unavailable, absent or unreported data.
- Missing values should not automatically be replaced with zero.

Transformations that alter this distinction must be explicitly documented.

## Coverage

Historical coverage varies by protocol, market and source.

The first available observation in a dataset represents available source coverage.

It does not automatically represent:

- market launch;
- protocol launch;
- token launch;
- beginning of adoption;
- or beginning of Brazilian activity.

Coverage should therefore be considered when constructing comparable analytical periods.

## Analytical Principle

The data dictionary separates:

Observed fields
    ↓
Derived metrics
    ↓
Interpretation

The meaning of a field comes from the source data and its documented definition, not from the narrative the analysis may eventually produce.
