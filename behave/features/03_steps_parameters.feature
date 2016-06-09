Feature: Steps Parameters

  Scenario Outline: Use Blender with <this>
    Given I put "<this>" in a blender
    When I switch the blender on
    Then It should transform into "<that>"

    Examples: Amphibians
      | this          | that |
      | red tree frog | mush |

    Examples: Consumer Electronics
      | this   | that        |
      | iPhone | toxic waste |
      | nexus  | toxic waste |

    Examples: Fruits
      | this    | that         |
      | apples  | apple juice  |
      | oranges | orange juice |
