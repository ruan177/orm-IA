from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

URL = "mysql+mysqlconnector://root:residentevil6@localhost:3306/ORM_1N_N1"

# $ cd C:\Program Files\MySQL\MySQL Server 8.0\bin
# $ .\mysql.exe -u aluno -p
# mysql> CREATE DATABASE ORM_1N_N1;
# mysql> USE ORM_1N_N1;
# mysql> SHOW TABLES;
Base = declarative_base()


class Player(Base):
    __tablename__ = "Player"
    id_player = Column(Integer, primary_key=True)
    nome = Column(String(150), nullable=False)

    characters = relationship("Character", backref="player")
    accounts = relationship("Account", backref="player")
    playergame = relationship("player_Game", backref="player")

    def __str__(self):  
        return "Player(id_player={}, nome=\"{}\")".format(
            self.id_player, self.nome)


class Character(Base):
    __tablename__ = "Character"
    id_character = Column(Integer, primary_key=True)
    nome = Column(String(150), nullable=False)
    level = Column(String(150), nullable=False)
    exp = Column(String(150), nullable=False)
    damage = Column(String(150), nullable=False)
    life = Column(String(150), nullable=False)
    classe = Column(String(150), nullable=False)

    gamecharacter = relationship("game_Character", backref="character")

    id_player = Column(Integer, ForeignKey("Player.id_player"))

    def __str__(self):
        return "Character(id_character={}, nome=\"{}\", level=\"{}\", exp=\"{}\", damage=\"{}\", life=\"{}\", classe=\"{}\")".format(
            self.id_character, self.nome, self.level, self.exp, self.damage, self.life, self.classe)

class Game(Base):
    __tablename__ = "Game"
    id_game = Column(Integer, primary_key=True)
    nome = Column(String(150), nullable=False)

    playergame = relationship("player_Game", backref="game")
    gamecharacter = relationship("game_Character", backref="game")
    progress = relationship("PlayerProgress", backref="game")
    sessions = relationship("gameSession", backref="game")

    def __str__(self):
        return "Game(id_game={}, nome=\"{}\")".format(
            self.id_game, self.nome)

class Account(Base):
    __tablename__ = "Account"
    id_account = Column(Integer, primary_key=True)
    nome = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False)
    password = Column(String(150), nullable=False)

    id_player = Column(Integer, ForeignKey("Player.id_player"))
    progress = relationship("PlayerProgress", backref="account")

    def __str__(self):
        return "Account(id_account={}, nome=\"{}\", email=\"{}\", password=\"{}\")".format(
            self.id_account, self.nome, self.email, self.password)



class gameSession(Base):
    __tablename__ = "GameSession"
    id_gamesession = Column(Integer, primary_key=True)
    startime = Column(String(150), nullable=False)
    endtime = Column(String(150), nullable=False)
    session = Column(Integer, nullable=False)

    id_game = Column(Integer, ForeignKey("Game.id_game"))

    def __str__(self):
        return "GameSession(id_gamesession={}, startime=\"{}\", endtime=\"{}\", session=\"{}\")".format(
            self.id_gamesession, self.startime, self.endtime, self.session)

class PlayerProgress(Base):
    __tablename__ = "GameProgress"
    id_playerprogress = Column(Integer, primary_key=True)
    levelend = Column(Integer, nullable=False)
    timeReading = Column(String(150), nullable=False)
    qntErros = Column(Integer, nullable=False)
    qntdies = Column(Integer, nullable=False)

    id_game = Column(Integer, ForeignKey("Game.id_game"))
    id_account = Column(Integer, ForeignKey("Account.id_account"))


    def __str__(self):
        return "GamePogress(id_playerprogress={}, levelend=\"{}\", timeReading=\"{}\", qntErros=\"{}\", qntdies=\"{}\")".format(
            self.id_playerprogress, self.levelend, self.timeReading, self.qntErros, self.qntdies)

class game_Character(Base):
    __tablename__ = "game_Character"
    id_gamecharacter = Column(Integer, primary_key=True)
    id_game = Column(Integer, ForeignKey("Game.id_game"))
    id_character = Column(Integer, ForeignKey("Character.id_character"))

    def __str__(self):
        return "GameCharacter(id_gamecharacter={}, id_game=\"{}\", id_character=\"{}\")".format(
            self.id_gamecharacter, self.id_game, self.id_character)

class player_Game(Base):
    __tablename__ = "player_Game"
    id_playergame = Column(Integer, primary_key=True)
    id_player = Column(Integer, ForeignKey("Player.id_player"))
    id_game = Column(Integer, ForeignKey("Game.id_game"))

    def __str__(self):
        return "PlayerGame(id_playergame={}, id_player=\"{}\", id_game=\"{}\")".format(
            self.id_playergame, self.id_player, self.id_game)


def main():
    engine = create_engine(url=URL)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    # mysql> DESC Pessoa;

    Session = sessionmaker(engine, expire_on_commit=False)

    with Session.begin() as session:
        player = Player(nome="John")

        player.characters.append(
           Character(nome="Parry", level= "1" , exp="10", damage="20", life="100", classe="Archiever"))
        player.characters.append(
            Character(nome="Stab", level="2", exp="10", damage="30", life="150", classe="Explorer"))

        player.accounts.append(
            Account(nome="Marc", email="facres@gmail.com", password="312321"))
        player.accounts.append(
            Account(nome="darc", email="hgfhfg@gmail.com", password="423423"))

        session.add(player)

    with Session.begin() as session:

       print("============================================")

       player = session.query(Player).get(1)

       print(player)

       for character in player.characters:
           print("   * " + str(character))

       for account in player.accounts:
           print("   * " + str(account))

    with Session.begin() as session:
        game = Game(nome="Dungeons and Dragons")

        game.sessions.append(
            gameSession(startime = "0:00", endtime = "200:21", session=123))
        game.sessions.append(
            gameSession(startime="0:00", endtime="100:24", session=321))

        game.progress.append(
            PlayerProgress(levelend=132, timeReading="15:13" ,qntErros=12, qntdies=2)
        )
        game.progress.append(
            PlayerProgress(levelend=200, timeReading="11:36", qntErros=5, qntdies=5)
        )

        session.add(game)

    with Session.begin() as session:

        print("============================================")

        game = session.query(Game).get(1)

        print(game)

        for progress in game.progress:
            print("   * " + str(progress))

        for session in game.sessions:
            print("   * " + str(session))

    with Session.begin() as session:
        game_character = game_Character(id_game=1, id_character=1)
        session.add(game_character)

    with Session.begin() as session:

        print("============================================")

        game_character = session.query(game_Character).get(1)

        print(str(game_character))


    with Session.begin() as session:
        player_game = player_Game(id_game=1, id_player=1)
        session.add(player_game)

    with Session.begin() as session:

        print("============================================")

        player_game = session.query(player_Game).get(1)

        print(str(player_game))


if __name__ == "__main__":
    main()
