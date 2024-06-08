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
    // the valid computer-controlled enemy types available in the game
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
    // behaviours common to all game characters (i.e. to both Players and Enemies)
    fn describe(&self) -> String;
    fn take_damage(&mut self, damage_amount: u16);
}

impl GameCharacter for Player {
    // implement game character behaviours for the player object
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

fn describe_game_character(character: &impl GameCharacter) {
    println!("Description: {}", character.describe())
}

fn main() {
    let mut player = Player::new(PlayerClass::Sorceror);
    describe_game_character(&player);
    player.take_damage(2);
    describe_game_character(&player);
    player.take_damage(2);
    describe_game_character(&player);
}
