source .env

echo "**********"
echo "Running tests"

num_tests=$NUMBER_OF_TESTS
successes=$SUCCESSFUL_TESTS

echo "successes: $SUCCESSFUL_TESTS"
echo "num_tests: $NUMBER_OF_TESTS"


if [ "$successes" = "$num_tests" ]; then
    echo "All tests passed!"
else
    echo "Not all tests passed"
fi

echo "**********"





echo "**********"