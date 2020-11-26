

CREATE TABLE IF NOT EXISTS users (
    id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    email VARCHAR(320) UNIQUE NOT NULL,
    password VARCHAR(60) NOT NULL
);
CREATE TABLE IF NOT EXISTS items (
    id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title VARCHAR(320) UNIQUE NOT NULL,
    uin VARCHAR(20) UNIQUE NOT NULL,
    lowest NUMERIC
);
CREATE TABLE IF NOT EXISTS users_items (
    user_id integer NOT NULL,
    item_id integer NOT NULL,
    target_price NUMERIC NOT NULL
);
CREATE TABLE IF NOT EXISTS prices (
    item_id integer NOT NULL,
    price NUMERIC NOT NULL,
    times_tamp timestamp NOT NULL DEFAULT NOW()
);
