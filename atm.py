from collections import defaultdict

import pytest

COINS = [200, 100, 50, 20, 10, 5, 2, 1]


def get_minimal_coins(total_amount_in_cents: int) -> dict[int, int]:
    if total_amount_in_cents < 0:
        raise ValueError("only positive amounts are supported")

    returned_coins = defaultdict(lambda: 0)
    remaining_amount = total_amount_in_cents

    for coin in COINS:
        while remaining_amount >= coin:
            returned_coins[coin] += 1
            remaining_amount -= coin

    return returned_coins


def test_should_get_no_coins_for_zero_amount():
    assert get_minimal_coins(0) == {}, "no money is returned"


def test_should_raise_error_when_negative_value_is_given():
    with pytest.raises(ValueError):
        get_minimal_coins(-1)


def test_should_get_single_coin_when_coin_with_that_value_exists():
    for amount in COINS:
        assert get_minimal_coins(amount) == {amount: 1}, (
            f"{amount} should return a single coin"
        )


def test_should_return_multiple_coins_with_different_values():
    result = get_minimal_coins(3)
    assert len(result) == 2
    assert result == {1: 1, 2: 1}


def test_should_return_multiple_coins_with_same_value_when_required():
    assert get_minimal_coins(4) == {2: 2}
