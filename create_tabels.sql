

CREATE TABLE IF NOT EXISTS items (
    id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title VARCHAR(320) NOT NULL,
    price VARCHAR(320) NOT NULL,
    lowest VARCHAR(320) NOT NULL,
    time timestamp NOT NULL DEFAULT NOW()
);
CREATE TABLE IF NOT EXISTS users (
    id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    email VARCHAR(320) UNIQUE NOT NULL,
    password varchar(30) NOT NULL
);
CREATE TABLE IF NOT EXISTS users_items (
    user_id integer NOT NULL,
    item_id integer NOT NULL,
    target_price integer NOT NULL
);
CREATE TABLE IF NOT EXISTS prices (
    item_id integer NOT NULL,
    price integer UNIQUE NOT NULL,
    time timestamp NOT NULL
);
