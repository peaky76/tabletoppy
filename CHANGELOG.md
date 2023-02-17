# Changelog

## 0.2.1 (2023-02-17)

#### Refactorings

- convert Coin.Face Enum to functional syntax
- add Randomisable abstract base class
- make Coin subclass of Randomiser
- make Die subclass of Randomiser

#### Other

- implement type checking with mypy

## 0.2.0 (2023-02-15)

#### New Features

- add Die class
- add .face property to Die
- add .roll method to Die

#### Docs

- change style to readthedocs theme
- extra metadata in pyproject.toml

## 0.1.0 (2023-02-14)

#### New Features

- add Coin class
- add .toss method to Coin
- add .turn method to Coin
- add .is_heads and .is_tails methods to Coin
- add str dunder method to Coin
