from sqlmodel import SQLModel, Field, create_engine, Session

sqlite_file_name = "database.db"  
sqlite_url = f"sqlite:///{sqlite_file_name}"  


class Guild(SQLModel, table=True):
    id: int| None = Field(default=None, primary_key=True)

    base_amount:    int | None = Field(default=500)
    allowed_debt:   int | None = Field(default=0)


class Account(SQLModel, table=True):
    id:             int | None = Field(default=None, primary_key=True)
    
    guild_id:       int | None = Field(foreign_key="guild.id")
    user_id:        int

    money:          int


class Item(SQLModel, table=True):
    id:             int | None = Field(default=None, primary_key=True)

    creator_id:     int | None = Field(foreign_key="account.id")
    owner_id:       int | None = Field(foreign_key="account.id")

    name:           str
    desc:           str | None

    in_shop:        bool | None = Field(default=False)


engine = create_engine(sqlite_url)

SQLModel.metadata.create_all(engine)

def getSession() -> Session:
    return Session(engine)
