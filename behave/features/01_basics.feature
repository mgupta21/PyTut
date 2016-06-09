Feature: Showing off behave

Scenario: Run a simple test
  Given we have behave installed
  When we implement a test
  Then behave will test it for us


# Running :
#   behave features/01_basics.feature
#   behave --format=plain --show-timings features/01_basics.feature