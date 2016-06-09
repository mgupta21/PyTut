Feature: Steps Parameters

  Scenario Outline: Blenders
    Given I put <thing> in a blender
    When I switch the blender on
    Then It should transform into <other thing>

    Examples: Amphibians
      | thing         | other thing |
      | red tree frog | mush        |

    Examples: Consumer Electronics
      | thing  | other thing |
      | iPhone | toxic waste |
      | nexus  | toxic waste |

    Examples: Fruits
      | thing   | other thing  |
      | apples  | apple juice  |
      | oranges | orange juice |
