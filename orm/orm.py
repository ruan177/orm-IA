from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

URL = "mysql+mysqlconnector://root:residentevil6@localhost:3306/ORM"

# $ cd C:\Program Files\MySQL\MySQL Server 8.0\bin
# $ .\mysql.exe -u aluno -p
# mysql> CREATE DATABASE ORM;
# mysql> USE ORM;
# mysql> SHOW TABLES;
Base = declarative_base()


class Player(Base):
    __tablename__ = "Player"
    id_player = Column(Integer, primary_key=True)
    nome = Column(String(150), nullable=False)


class Character(Base):
    __tablename__ = "Character"
    id_character = Column(Integer, primary_key=True)
    nome = Column(String(150), nullable=False)
    level = Column(Integer, nullable=False)
    exp = Column(Integer, nullable=False)
    damage = Column(Integer, nullable=False)
    life = Column(Integer, nullable=False)
    classe = Column(String(150), nullable=False)
    id_

class Game(Base):
    __tablename__ = "Game"
    id_game = Column(Integer, primary_key=True)
    nome = Column(String(150), nullable=False)




class Account(Base):
    __tablename__ = "Account"
    id_account = Column(Integer, primary_key=True)
    nome = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False)
    password = Column(String(150), nullable=False)

class gameSession(Base):
    __tablename__ = "GameSession"
    id_gamesession = Column(Integer, primary_key=True)
    startime = Column(String(150), nullable=False)
    endtime = Column(String(150), nullable=False)
    session = Column(Integer, nullable=False)

class PlayerProgress(Base):
    __tablename__ = "GameProgress"
    id_playerprogress = Column(Integer, primary_key=True)
    levelend = Column(Integer, nullable=False)
    timeReading = Column(String(150), nullable=False)
    qntErros = Column(Integer, nullable=False)
    qntdies = Column(Integer, nullable=False)


def main():
    engine = create_engine(url=URL)
    # Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    # mysql> DESC Pessoa;

    Session = sessionmaker(engine, expire_on_commit=False)

    with Session.begin() as session:
        player = Player(nome="Jhon Snow")
        id_player = player.id_player
        session.add(player)

    with Session.begin() as session:
        game = Game(nome='Ludic Histiores of Past')
        id_game = game.id_game
        session.add(game)

    with Session.begin() as session:
        character = Character(nome='joazinho',level=10, exp=320, damage=45, life=100, classe='Archiever')
        id_character = character.id_character
        session.add(character)

    with Session.begin() as session:
        gamesession = gameSession(startime=4324, endtime=4234, session=24)
        id_gamesession = gamesession.id_gamesession
        session.add(gamesession)

    with Session.begin() as session:
        playerprogress = PlayerProgress(levelend=23, timeReading=345, qntErros=13, qntdies=50)
        id_playerprogress = playerprogress.id_playerprogress
        session.add(playerprogress)

    with Session.begin() as session:
        account = Account(nome='Aleatorio123', email='aleatiorio@gmail.com', password='12345')
        id_account = account.id_account
        session.add(playerprogress)

if __name__ == "__main__":
    main()
