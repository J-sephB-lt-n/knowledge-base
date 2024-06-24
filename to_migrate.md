# Knowledge Base

Whenever I discover something interesting or useful, but is too small to be it's own project, then I put it into here.

I've put the sections links in a disordered heap to make serendipity more likely:

[OAuth2.0](#oauth-20), [Association, Bias & Causation](#association-bias--causation), [Algorithms list](#algorithms-list), [Database Normalisation (incomplete)](#database-normalisation), [Learning Resources](#learning-resources), [product value proposition frameworks (incomplete)](#product-value-proposition-frameworks), [Cool open-source software tools](#cool-open-source-software-tools), [useful bash terminal commands](#useful-bash-terminal-commands), [useful regex patterns](#useful-regex-patterns), [open-source data annotation tools](#open-source-data-annotation-tools), [Rust Traits Example](#rust-traits-example)

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

## Product Value Proposition Frameworks

People will buy anything which they perceive to have high value to them (example: people buy bottled tap water).

These frameworks are all taken from the Harvard Innovation Labs YouTube video [Value Props: Create a Product People Will Actually Buy](https://youtu.be/q8d9uuO1Cf4)

Value Proposition Statement (it is important to explicitly define the problem being solved):

- For (target customer segments)

- dissatisfied with (existing solution)

- due to (key unmet needs)

- (Venture name) offers a (product category)

- that provides (key benefits of your solution)

**Minimum Viable Segment**:

- TODO

**4U Framework**: Problems worth solving are:

- Unworkable (i.e. if the problem is not solved then the consequences are measurable and material)

- Unavoidable (the problem must be addressed by the customer e.g. tax, regulation, medical condition)

- Urgent (problem is at the top of the customer's priority list)

- Underserved (demand for a solution exceeds supply - customers do not have adequate access to good solutions for this problem)

**BLAC & White Framework**: Define the market need:

- "Blatant" problems are ones which are obvious to the customer (don't need to educate/convince the customer of the problem)

- "Latent" problems are ones which the customer is unaware (or not fully aware) of (they must be convinced of/educated about the problem)

- "Aspirational" needs are a customer's needs for success, prestige and social status (desirable but not urgent)

- "Critical" needs are ones which must be urgently fulfilled

|                    |             | CUSTOMER NEED                                               |                                                                               |
| ------------------ | ----------- | ----------------------------------------------------------- | ----------------------------------------------------------------------------- |
|                    |             | **Aspirational**                                            | **Critical**                                                                  |
| PROBLEM VISIBILITY | **Blatant** | luxury goods                                                | obvious need (accounting, healthcare)                                         |
|                    | **Latent**  | new products for yet to be recognised needs (e.g. new tech) | important need, but not yet fully recognised by the customer (e.g. insurance) |

**DEBT Framework**: WTF is this

- Dependencies: On what external systems/resources does my solution rely in order to function? (e.g. electric cars rely on the availability of public charging stations, a cellphone needs a mobile network carrier)

- External factors: Are there things acting outside of my control which can affect the effectiveness of my solution? (e.g. new data privacy regulations, availability of component parts, economic conditions, exchange rate fluctuations)

- Backlash: Are there individuals or communities who are likely to react adversely to the release of my product? (e.g. workers made obsolete by an automation solution)

- Timing: When is the best time to launch? A product can be unsuccessful through early launch or late launch, or by missing or coinciding with some relevant event (e.g. competitor launch or cultural event).

**3D Framework**:

- Disruptive: Does the product displace existing solutions/competitors? (e.g. uber's effect on the taxi industry, or netflix on dvd-rentals)

- Discontinuous:

- Defensible:

**Before/After** & **Gain/Pain Ratio**:

- > &geq; 10 to overcome inertia and risk

**Bringing it all together**

- TODO
