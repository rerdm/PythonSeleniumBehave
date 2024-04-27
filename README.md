# PythonSeleniumBehave

### Preconditions

1. Install Gherkin-Plugin in > File > Settings > Plugins > Gherkin (IntelliJ)
2. Install Selenium : ``pip install selenium``
3. Install Selenium : ``pip install behave``
----
###  Creating Feature-File ( Given , When, Then, And, But )

1. Crate Feature-File and saveit as:  `your_name.feature`

```
Feature: Login as valid user (Test-Set)
    Scenario: login an existing user ( Test-Case )
        
            Given I go to the Login page
            When I click on login 
            Then I should see error
```
----

### Creating Step-Definition file 

- Generate a step definition template for all feature-files in the current dir.``behave``
- Genrate a step definition template file for specific feature-file in the current dir ``behave test.feature``
- Genrate a step definition template for a feature file in a specific dir ``behave examples/test.feature``
- The generated files are just a template and has to be adapted before running.

```
You can implement step definitions for undefined steps with these snippets:

@given(u'I create a new user')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I create a new user')


@when(u'I type email')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I type email')


@when(u'I type password')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I type password')


@when(u'I click on \'Login\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on \'Login\'')


@then(u'I should see teh text welcome')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see teh text welcome')

```

----

### Run the test with behave

1. From commandline with no print out: ``behave test.feature``
2. From commandline with print out(all tests): ``behave``

```
Feature: Logging in with valid credentials # test.feature:1

  Scenario: User login in successfully  # test.feature:2
    Given I create a new user           # steps/steps.py:5
    When I type email                   # steps/steps.py:11
    When I type password                # steps/steps.py:17
    When I click on 'Login'             # steps/steps.py:23
    Then I should see teh text welcome  # steps/steps.py:29

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
5 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.003s

```

3. From commandline with print out : ``behave test.feature --no-capture``
4. From commandline with no print out( all tests): ``behave``


```
Feature: Logging in with valid credentials # test.feature:1

  Scenario: User login in successfully  # test.feature:2
    Given I create a new user           # steps/steps.py:5
    When I type email                   # steps/steps.py:11
    When I type password                # steps/steps.py:17
    When I click on 'Login'             # steps/steps.py:23
    Then I should see teh text welcome  # steps/steps.py:29

1 feature passed, 0 failed, 0 skipped
  Scenario: User login in successfully  # test.feature:2
    Given I create a new user           # steps/steps.py:5
I create a new user
    When I type email                   # steps/steps.py:11
I type email
    When I type password                # steps/steps.py:17
I type password
    When I click on 'Login'             # steps/steps.py:23
click on 'Login'
    Then I should see teh text welcome  # steps/steps.py:29
I should see teh text welcome

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
5 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.003s

````


