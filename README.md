# Knowledge Base

Whenever I discover something interesting or useful, but is too small to be it's own project, then I put it into here.

I've put the sections links in a disordered heap to make serendipity more likely:

[OAuth2.0](#oauth-20), [Association, Bias & Causation](#association-bias--causation), [Algorithms list](#algorithms-list), [Database Normalisation (incomplete)](#database-normalisation), [Kelly Criterion](#the-kelly-criterion), [Learning Resources](#learning-resources), [Cool open-source software tools](#cool-open-source-software-tools), [useful bash terminal commands](#useful-bash-terminal-commands), [useful regex patterns](#useful-regex-patterns), [open-source data annotation tools](#open-source-data-annotation-tools), [Rust Traits Example](#rust-traits-example)

## Algorithms List

| Name                                    | Description                                                 | Example Use Cases       | Useful Resources                                                                                                     |
| --------------------------------------- | ----------------------------------------------------------- | ----------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Anomaly Detection                       |                                                             | payment fraud detection | <https://scikit-learn.org/stable/modules/outlier_detection.html>                                                     |
| Bayesian Hierarchical Modelling         |                                                             |                         |
| Bayesian Networks                       |                                                             |                         |
| Causal (decision) Bayesian Networks     |                                                             |                         |
| Clustering                              |                                                             |                         |
| Collaborative Filtering                 |                                                             |                         |
| Computer Vision: Image Classification   |                                                             |                         | <https://huggingface.co/models>                                                                                      |
| Computer Vision: Image Segmentation     |                                                             |                         | <https://huggingface.co/models>                                                                                      |
| Computer Vision: Object Detection       |                                                             |                         | <https://huggingface.co/models>                                                                                      |
| Confidence/Credibility Intervals        |                                                             |                         |
| Data Drift                              |                                                             |                         | see also: "Population Stability Index" (PSI), "KL Divergence"                                                        |
| Dimension Reduction                     |                                                             |                         |
| Document Question Answering             |                                                             |                         | <https://huggingface.co/models>                                                                                      |
| Hypothesis Testing                      |                                                             |                         |
| Image Generation (image variation)      |                                                             |                         | <https://huggingface.co/models>                                                                                      |
| Image Generation (text prompt)          |                                                             |                         | <https://huggingface.co/models>                                                                                      |
| Knowledge Graphs                        |                                                             |                         |
| Mathematical Optimisation               |                                                             |                         |
| Multi-Armed Bandit Algorithms           |                                                             |                         |
| Optical Character Recognition (OCR)     | Read text from an image                                     |                         | <https://github.com/kba/awesome-ocr> (the [tesseract](https://github.com/tesseract-ocr/tesseract) engine is amazing) |
| Retrival-Augmented Generation (RAG)     |                                                             |                         |
| Sequential Hypothesis Testing           | Cost-effective experimentation through valid early stopping |                         | <https://en.wikipedia.org/wiki/Sequential_analysis>                                                                  |
| Shrinkage Estimators (e.g. James Stein) |                                                             |                         |
| Supervised Learning                     |                                                             |                         |
| Survival Analysis                       |                                                             |                         |
| Topic Modelling (NLP)                   |                                                             |                         |

## Learning Resources

| Is Free | Name                                                  | Description                                                                                   | Link(s)                                                                                                                  |
| ------- | ----------------------------------------------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Yes     | Awesome Time Series                                   | A large curated list of time series resources                                                 | <https://github.com/lmmentel/awesome-time-series>                                                                        |
| Yes     | Big Book of R                                         | A staggeringly large repository of Data Science, Machine-Learning and statistics books        | <https://www.bigbookofr.com>                                                                                             |
| Yes     | Causal Inference: The Mixtape                         | (book) Modeling techniques for causal inference                                               | <https://mixtape.scunning.com/>                                                                                          |
| Yes     | The Effect                                            | (book) An Introduction to Research Design and Causality                                       | <https://theeffectbook.net/>                                                                                             |
| Yes     | Forecasting: Principles and Practice                  | A thorough summary of a wide range of time series forecasting topics (with R code)            | <https://robjhyndman.com/teaching/> or <https://otexts.org/fpp3/>                                                        |
| Yes     | Google user authentication and password best practice | 13 best practices for user account, authentication, and password management                   | <https://cloud.google.com/blog/products/identity-security/account-authentication-and-password-management-best-practices> |
| Yes     | jwt.io                                                | Amazing interactive resource for learning about Json Web Tokens (JWTs)                        | <https://jwt.io>                                                                                                         |
| Yes     | Made With ML                                          | Beautifully curated content (with code examples) on the full Data + Machine Learning Pipeline | <https://madewithml.com/>                                                                                                |
| Yes     | OWASP                                                 | A global open organization dedicated to cyber security                                        | <https://owasp.org>                                                                                                      |
| Yes     | OWASP Cheat Sheet Series                              | Articles covering a large range of web security topics                                        | <https://github.com/OWASP/CheatSheetSeries>                                                                              |
| Yes     | OWASP Web Security Testing Guide                      | Guide to assessing the security of a web application                                          | <https://github.com/OWASP/wstg>                                                                                          |
| Yes     | Relational Database Normalisation                     | A very clear explanation of the first 5 normal forms                                          | <https://www.youtube.com/watch?v=GFQaEYEc8_8>                                                                            |
| Yes     | RestfulAPI.net                                        | A wealth of information on REST API architecture and design                                   | <https://restfulapi.net/>                                                                                                |
| Yes     | Tech Interview Handbook                               |                                                                                               | <https://github.com/yangshun/tech-interview-handbook>                                                                    |

## Cool Open Source Software Tools

| Name               | Description                                                                                | Link(s)                                                                                                      |
| ------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| Black              | Auto-formatting (standardization) of python code                                           |
| Commitizen         | For standardizing git commit messages                                                      | <https://github.com/commitizen-tools/commitizen> (see also <https://www.conventionalcommits.org/en/v1.0.0/>) |
| DuckDB             |                                                                                            |
| EGADS              | Open-source Java package to automatically detect anomalies in large scale time-series data | <https://github.com/yahoo/egads>                                                                             |
| Great Expectations |                                                                                            | <https://github.com/great-expectations/great_expectations>                                                   |
| HuggingFace        |                                                                                            | <https://huggingface.co>                                                                                     |
| ML Flow            | For managing Machine Learning models in production                                         |
| PyLint             | For automatic assessment of python code quality                                            |
| PyMC               | For bayesian modelling in python                                                           |
| Scalene            | Python program profiling (for speed/memory optimization)                                   | <https://github.com/plasma-umass/scalene>                                                                    |
| Sci-Kit Learn      | Established python Machine Learning framework                                              |
| Scrapy             | Established python framework for web scraping                                              | <https://github.com/scrapy/scrapy>                                                                           |
| SQLite             | In-file SQL database                                                                       |
| Tesseract          | Extremely good Optical Character Recognition (OCR) engine                                  | <https://github.com/tesseract-ocr/tesseract>                                                                 |
| TS Fresh           | Automatic extraction of relevant features from time series                                 | <https://github.com/blue-yonder/tsfresh>                                                                     |

## Open-Source Data Annotation Tools

| Name      | Description                                          | Link(s)                               |
| --------- | ---------------------------------------------------- | ------------------------------------- |
| Brat      | online environment for collaborative text annotation | <https://brat.nlplab.org>             |
| Docanno   |                                                      | <https://github.com/doccano/doccano>  |
| Prodigy   |                                                      | <https://prodi.gy>                    |
| INCEpTION |                                                      | <https://inception-project.github.io> |

## Useful Bash Terminal Commands

| Task                                                            | Command                                                                                                               |
| --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Convert hex string to utf-8                                     | <code>echo 54657374696e672031203220330 &##124; xxd -r -p</code>                                                       |
| Find files by name (using regex)                                | `find . -name "*.sql"`                                                                                                |
| Remove all occurences of **pycache** folder                     | `find . -type d -name __pycache__ -exec rm -r {} \+`                                                                  |
| Replace text within a file (`/g` replaces all occurences)       | `sed -i "s/text_to_find/text_to_replace_with/g" myfile.txt` (i.e. same syntax as `:s` in [vim](https://www.vim.org/)) |
| Search for text within multiple files (within multiple folders) | `grep -r "search_string" /path/to/base/folder`                                                                        |

## Useful Regex Patterns

| Pattern                         | Explanation                    |
| ------------------------------- | ------------------------------ |
| ^\w[\w\.\-]+@(\w+\.)+[\w]{2,4}$ | Basic email address validation |

## Association, Bias & Causation

```math
$$\begin{array}{lcl}
\underbrace{E\Big[Y\Bigl|T=1\Big] - E\Big[Y\Bigl|T=0\Big]}_{
    \substack{ \text{Difference between} \\ \text{treatment group means} }
    }
    &=&
    \underbrace{E\Big[Y(1)-Y(0)\Bigl|T=1\Big]}_{
    \substack{\text{Average Treatment effect} \\ \text{on the Treated (ATT)} }} +
    \underbrace{\Bigg(E\Big[Y(0)\Bigl|T=1\Big]-E\Big[Y(0)\Bigl|T=0\Big]\Bigg)}_{
        \text{Selection Bias}
        } \\
\space &\space& \space \\
Y_i &=& \text{outcome of interest (on individual } i)\\
T_i &=& \begin{cases}1 \quad \text{if individual } i \text{ received treatment} \\
0 \quad \text{if individual } i \text{ did not receive treatment}\end{cases} \\
Y_i(1) &=& \text{outcome which would have been observed for individual } i \text{ if they had received the treatment} \\
Y_i(0) &=& \text{outcome which would have been observed for individual } i \text{ if they had NOT received the treatment} \\
\end{array}$$
```

Here is a simulation in python showing this to be true:

```python
import random
import statistics

N_INDIVIDUALS: int = 100_000
random.seed(69)

untreated_prob_of_dying: list[float] = [
    random.uniform(0, 1) for _ in range(N_INDIVIDUALS)
]
treated_prob_of_dying: list[float] = [
    # treatment halves probability of death #
    0.5 * p
    for p in untreated_prob_of_dying
]
assigned_treatment_group: list[str] = [
    # biased by probability of dying #
    random.choices(["treated", "untreated"], weights=(p, 1 - p))[0]
    for p in untreated_prob_of_dying
]
prob_of_dying: list[float] = [
    (
        untreated_prob_of_dying[idx]
        if treat_grp == "untreated"
        else treated_prob_of_dying[idx]
    )
    for idx, treat_grp in enumerate(assigned_treatment_group)
]
mean_prob_of_dying_treated_group: float = statistics.mean(
    [
        prob_of_dying[idx]
        for idx, treat_grp in enumerate(assigned_treatment_group)
        if treat_grp == "treated"
    ]
)
mean_prob_of_dying_untreated_group: float = statistics.mean(
    [
        prob_of_dying[idx]
        for idx, treat_grp in enumerate(assigned_treatment_group)
        if treat_grp == "untreated"
    ]
)
att: float = statistics.mean(
    [
        (treated_prob_of_dying[idx] - untreated_prob_of_dying[idx])
        for idx, treat_grp in enumerate(assigned_treatment_group)
        if treat_grp == "treated"
    ]
)
selection_bias: float = statistics.mean(
    [
        untreated_prob_of_dying[idx]
        for idx, treat_grp in enumerate(assigned_treatment_group)
        if treat_grp == "treated"
    ]
) - statistics.mean(
    [
        untreated_prob_of_dying[idx]
        for idx, treat_grp in enumerate(assigned_treatment_group)
        if treat_grp == "untreated"
    ]
)

print(
    f"""
                      E[Y|T=1] - E[Y|T=0] = {(mean_prob_of_dying_treated_group - mean_prob_of_dying_untreated_group):.5f}
                     ATT + selection_bias = {(att + selection_bias):.5f}

                    ATT: E[Y(1)-Y(0)|T=1] = {att:.5f}
Selection Bias: E[Y(0)|T=1] - E[Y(0)|T=0] = {selection_bias:.5f}
"""
)
```

```
                      E[Y|T=1] - E[Y|T=0] = 0.00176
                     ATT + selection_bias = 0.00176

                    ATT: E[Y(1)-Y(0)|T=1] = -0.33341
Selection Bias: E[Y(0)|T=1] - E[Y(0)|T=0] = 0.33516
```

## Database Normalisation

`<this section is still under construction>`

### 1st Normal Form

To be in first normal form, each table cell must contain a single value (e.g. not anything like an array, json or nested table within the cell).

Example: Not in first normal form:

| Name     | Skills                                |
| -------- | ------------------------------------- |
| Joe      | python,unicyling,piano                |
| Napoleon | nunchuck,bow hunting,computer hacking |

Example: In first normal form:

| Name     | Skill            |
| -------- | ---------------- |
| Joe      | python           |
| Joe      | unicyling        |
| Joe      | piano            |
| Napoleon | nunchuck         |
| Napoleon | bow hunting      |
| Napoleon | computer hacking |

### Database Normalisation: 2nd Normal Form

### Database Normalisation: 3rd Normal Form

## The Kelly Criterion

The [Kelly Criterion](https://en.wikipedia.org/wiki/Kelly_criterion) (or [Kelly Strategy](https://en.wikipedia.org/wiki/Kelly_criterion)) is a result from probability theory. In a specific repeated game (which resembles some gambling games and investment scenarios), it is the strategy achieving maximum gain/reward in the long run.

The formulation is as follows:

In a single game:

- The player invests (risks) $100r\%$ of their total assets/portfolio/wealth $A$.

- With probability $w$, they earn a return of $100g\%$ on their investment/risk. i.e. $A_{t+1}=A_t(1+rg)$

- With probability $1-w$, they lose $100b\%$ of their investment/risk. i.e. $A_{t+1}=A_t(1-rb)$

After playing $n$ consecutive games, the expected value of their total assets/portfolio/wealth is:

$$P_n \quad=\quad A_0(1+rg)^{wn}(1-rb)^{(1-w)n}$$

The value of $r$ maximizing $P_n$ can be found by solving the equation

$$\frac{d}{d r}\frac{log(P_n)}{n} \quad=\quad 0$$

The solution is:

$$arg\space max_r\space P_n \quad=\quad \displaystyle\frac{w}{b} - \frac{1-w}{g}$$

# Rust Traits Example

Here is an example showing how traits can be used to create shared behaviour between structs:

```bash
.
├── Cargo.lock
├── Cargo.toml
└── src
    └── main.rs
```

```toml
# Cargo.toml

[package]
name = "traits_example"
version = "0.1.0"
edition = "2021"

[dependencies]
strum = "0.26"
strum_macros = "0.26"
```

```rust
// src/main.rs

use strum_macros::Display;

#[derive(Display)]
enum PlayerClass {
    // available valid class choices for the human player
    Warrior,
    Rogue,
    Sorceror,
}

#[derive(Display)]
enum EnemyType {
    // available valid non-player types available
    Orc,
    Goblin,
    Necromancer,
    Troll,
}

struct Player {
    // object to hold information about the player state
    player_class: PlayerClass,
    hit_points: u16,
}

impl Player {
    fn new(player_class: PlayerClass) -> Self {
        // method for creating a new player
        let hit_points = match player_class {
            PlayerClass::Warrior => 10,
            PlayerClass::Rogue => 6,
            PlayerClass::Sorceror => 3,
        };

        Player {
            player_class,
            hit_points,
        }
    }
}

struct Enemy {
    // object containing information on the state of a non-player character
    enemy_type: EnemyType,
    hit_points: u16,
}

impl Enemy {
    fn new(enemy_type: EnemyType) -> Self {
        // method which creates a new enemy
        let hit_points = match enemy_type {
            EnemyType::Orc => 8,
            EnemyType::Goblin => 2,
            EnemyType::Necromancer => 3,
            EnemyType::Troll => 50,
        };

        Enemy {
            enemy_type,
            hit_points,
        }
    }
}

trait GameCharacter {
    // behaviours (methods) common to all game characters
    fn describe(&self) -> String;
    fn take_damage(&mut self, damage_amount: u16);
}

impl GameCharacter for Player {
    // implement game character behaviours (methods) for the player object
    fn describe(&self) -> String {
        format!(
            "player is a {} with {} hit point(s)",
            self.player_class, self.hit_points,
        )
    }

    fn take_damage(&mut self, damage_amount: u16) {
        if damage_amount >= self.hit_points {
            self.hit_points = 0;
        } else {
            self.hit_points -= damage_amount;
        }
        println!("player took {} damage", damage_amount);
    }
}

impl GameCharacter for Enemy {
    // implement game character behaviours (methods) for the enemy object
    fn describe(&self) -> String {
        format!(
            "enemy is a {} with {} hit point(s)",
            self.enemy_type, self.hit_points,
        )
    }

    fn take_damage(&mut self, damage_amount: u16) {
        if damage_amount >= self.hit_points {
            self.hit_points = 0;
        } else {
            self.hit_points -= damage_amount;
        }
        println!("enemy took {} damage", damage_amount);
    }
}

fn describe_game_character(game_character: &impl GameCharacter) {
    // Function which calls the describe() method of any object which has the `GameCharacter` trait
    println!("Description: {}", game_character.describe())
}

fn main() {
    let mut player = Player::new(PlayerClass::Sorceror);
    describe_game_character(&player);
    player.take_damage(2);
    describe_game_character(&player);
    player.take_damage(2);
    describe_game_character(&player);
    let mut enemy = Enemy::new(EnemyType::Troll);
    describe_game_character(&enemy);
    enemy.take_damage(15);
    describe_game_character(&enemy);
}
```

## OAuth 2.0

OAuth2.0 is an industry-standard protocol for authorization (i.e. managing access to protected HTTP resources).

OAuth2.0 can be used also for authentication (identifying who a user is) by extending it with [OIDC](#oidc)

I never properly understood OAuth2.0 until I read the RFC (6749), which is very well written.

Abstract from the RFC (6749):

```bash
The OAuth 2.0 authorization framework enables a third-party
application to obtain limited access to an HTTP service, either on
behalf of a resource owner by orchestrating an approval interaction
between the resource owner and the HTTP service, or by allowing the
third-party application to obtain access on its own behalf. This
specification replaces and obsoletes the OAuth 1.0 protocol described
in RFC 5849.
```

At a high-level:

- Oauth2.0 manages 3rd party client (e.g. Zoom) access to a subset of a resource owner's (e.g. end user's) protected resources (e.g. calendar only) which are stored on a resource server (e.g. gmail), without the 3rd party client (Zoom) having any access to the resource owner's (e.g. end user's) credentials (e.g. username and password).

- This is achieved through the use of an authorisation server. This authorisation server issues the client with temporary access to some of the resource owner's protected resources on the resource server by issuing the client with a temporary access token (this access token is accepted and trusted by the resource server).

Here are the roles defined in the RFC (RFC 6749):

```bash
1.1.  Roles

   OAuth defines four roles:

   resource owner
      An entity capable of granting access to a protected resource.
      When the resource owner is a person, it is referred to as an
      end-user.

   resource server
      The server hosting the protected resources, capable of accepting
      and responding to protected resource requests using access tokens.

   client
      An application making protected resource requests on behalf of the
      resource owner and with its authorization.  The term "client" does
      not imply any particular implementation characteristics (e.g.,
      whether the application executes on a server, a desktop, or other
      devices).

   authorization server
      The server issuing access tokens to the client after successfully
      authenticating the resource owner and obtaining authorization.
```

Here is the oauth2.0 flow at a slightly deeper level:

I will use the example of a social media website (client) logging in an end-user (resource owner) using their google account (resource server).

1. Client (social media website) requests access to user's name, Google ID and gmail address (protected resource) from the resource owner (end-user)

2. Client (social media website) receives an authorisation grant, which is a credential representing the resource owner's (end-user's) authorisation

3. Client (social media website) presents their authorisation grant to the authorisation server in return for an access token

4. Client (social media website) requests the protected resource (user's name, Google ID and gmail address) from the resource server (google), presenting the access token

5. The resource server (google) validates the client (social media website) request and, if valid, serves the request

There are 4 different types of authorisation grants defined in RFC 6749:
(I will give an example usage of each immediately after)

| Grant Type                                      | Description                                                                                                                                                                                                                                                         | Example use case                                                             |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| Authorization code                              | A convoluted flow in which the authorisation server acts as intermediary (middleman) between client and resource owner.<br>This is a very secure choice, and the one you always encounter online<br>(OAuth2.0 recommends to extend this grant type to include PKCE) | A web-based platform allows users to authenticate using their Google account |
| Client credentials                              | The client itself has credentials which can be used to directly obtain an access token from the authorisation server.                                                                                                                                               | A microservice fetching data from a database                                 |
| DEPRECATED: Implicit                            | A simplified version of the Authorisation Code flow, which sacrifies security to achieve less calls to the authorisation server                                                                                                                                     |
| DEPRECATED: Resource owner password credentials | The client uses resource owner password credentials directly in order to directly obtain an access token.                                                                                                                                                           |

Explanation of the OAuth2.0 Authorisation Code flow, using the example of a web platform allowing a user to log in to the platfom using their Google account:

0. The client (website) must first register itself with the authorisation server (it will be given a unique client ID and client secret).

1. The client (website) makes a request to the authorisation server to access some of the resource owner's resources (end-user name and google ID). It does this by constructing a URL for the resource owner (end-user) to navigate to in their browser. This request contains required information such as the client ID, client secret, authorisation scope etc.

2. On navigating to the URL, the end-user is prompted by the authorisation server to approve the client (website) request. If they do, they are redirected back to the client (website). The URI to redirect them back to is specified by the client in their initial request to the authorisation server (step 1. above).

3. The authorisation server adds additional query parameters to the client (website) URI which the resource owner (end-user) is redirected back to (in step 2. above):

   - "code": An authorisation code which the client (website) can now use to get access tokens from the authorisation server

   - "state": This is a random string which was included in the original client (website) request to the authorisation server. The authorisation server must ensure that this matches the string which they sent in the original request (step 1. above).

4. The client (website) can now exchange the authorisation code (received in step 3. above) on the authorisation server for a short-lived access token, which it can use to access the resource owner's (end-user's) protected resources without having to ask them for permission again.

5. (optional) Optionally, the request in step 3. above can return an access token **and** a refresh token. A refresh token is a token which the client (website) can use to generate a new access token when the current one has expired. This helps to provide a better user experience (the resource owner doesn't have to re-authorise in all the time).

For a precise description on this process, refer to <https://developer.okta.com/blog/2018/04/10/oauth-authorization-code-grant-type>

## OIDC

Open ID Connect (OIDC):

- is a protocol for user authentication and identity management (i.e. validating the identity of an entity, such as a user, and accessing their attributes)

- is an identity layer built on top of [OAuth2.0](#oauth-20)

- allows 3rd-party applications to verify the identity of the end-user and to obtain basic user profile information

- is secure, centralised, and standardised

- uses [JWTs](https://github.com/J-sephB-lt-n/jwt-checkout/tree/main)

- defines how applications (e.g. a web-based platform) and identity providers (authentication servers) interact in order to establish secure end-user authentication

- is just OAuth2.0 with an additional token (ID token), and extra process for dealing with it (i.e. dictates the required structure of the ID token, how the ID token should be validated by the client etc.)

In the step in an OAuth2.0 flow where an access token is returned, OIDC returns an additional token (an ID token, in the form of a JWT).

Here is the official spec: <https://openid.net/specs/openid-connect-core-1_0.html>

I also enjoyed this: [The OIDC Handbook](https://auth0.com/resources/ebooks/the-openid-connect-handbook)
