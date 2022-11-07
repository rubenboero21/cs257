--
-- PostgreSQL database dump
--

-- Dumped from database version 14.5 (Homebrew)
-- Dumped by pg_dump version 14.5 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: abilities; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.abilities (
    id integer NOT NULL,
    name text
);


--
-- Name: abilities_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.abilities_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: abilities_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.abilities_id_seq OWNED BY public.abilities.id;


--
-- Name: egg_groups; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.egg_groups (
    id integer NOT NULL,
    name text
);


--
-- Name: egg_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.egg_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: egg_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.egg_groups_id_seq OWNED BY public.egg_groups.id;


--
-- Name: generations; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.generations (
    id integer NOT NULL,
    name text
);


--
-- Name: generations_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.generations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: generations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.generations_id_seq OWNED BY public.generations.id;


--
-- Name: legendaries; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.legendaries (
    id integer NOT NULL,
    name text
);


--
-- Name: legendaries_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.legendaries_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: legendaries_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.legendaries_id_seq OWNED BY public.legendaries.id;


--
-- Name: linking_table; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.linking_table (
    pokemon_id integer,
    type1_id integer,
    type2_id integer,
    ability1_id integer,
    ability2_id integer,
    ability3_id integer,
    egg_group1_id integer,
    egg_group2_id integer,
    legendary_id integer,
    specie_id integer,
    height double precision,
    weight double precision,
    catch_rate double precision,
    normal_resist double precision,
    fire_resist double precision,
    water_resist double precision,
    electric_resist double precision,
    grass_resist double precision,
    ice_resist double precision,
    fighting_resist double precision,
    poison_resist double precision,
    ground_resist double precision,
    flying_resist double precision,
    psychic_resist double precision,
    bug_resist double precision,
    rock_resist double precision,
    ghost_resist double precision,
    dragon_resist double precision,
    dark_resist double precision,
    steel_resist double precision,
    fairy_resist double precision
);


--
-- Name: pokemon; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.pokemon (
    id integer NOT NULL,
    dex_num integer,
    name text,
    hp integer,
    atk integer,
    spatk integer,
    def integer,
    spdef integer,
    spd integer
);


--
-- Name: pokemon_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.pokemon_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: pokemon_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.pokemon_id_seq OWNED BY public.pokemon.id;


--
-- Name: species; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.species (
    id integer NOT NULL,
    name text
);


--
-- Name: species_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.species_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: species_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.species_id_seq OWNED BY public.species.id;


--
-- Name: types; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.types (
    id integer NOT NULL,
    name text
);


--
-- Name: types_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.types_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: types_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.types_id_seq OWNED BY public.types.id;


--
-- Name: abilities id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.abilities ALTER COLUMN id SET DEFAULT nextval('public.abilities_id_seq'::regclass);


--
-- Name: egg_groups id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.egg_groups ALTER COLUMN id SET DEFAULT nextval('public.egg_groups_id_seq'::regclass);


--
-- Name: generations id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.generations ALTER COLUMN id SET DEFAULT nextval('public.generations_id_seq'::regclass);


--
-- Name: legendaries id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.legendaries ALTER COLUMN id SET DEFAULT nextval('public.legendaries_id_seq'::regclass);


--
-- Name: pokemon id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pokemon ALTER COLUMN id SET DEFAULT nextval('public.pokemon_id_seq'::regclass);


--
-- Name: species id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.species ALTER COLUMN id SET DEFAULT nextval('public.species_id_seq'::regclass);


--
-- Name: types id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.types ALTER COLUMN id SET DEFAULT nextval('public.types_id_seq'::regclass);


--
-- Data for Name: abilities; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.abilities (id, name) FROM stdin;
1	none
2	overgrow
3	chlorophyll
\.


--
-- Data for Name: egg_groups; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.egg_groups (id, name) FROM stdin;
1	none
2	grass
3	monster
\.


--
-- Data for Name: generations; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.generations (id, name) FROM stdin;
1	generation_1
2	generation_2
3	generation_3
4	generation_4
5	generation_5
6	generation_6
7	generation_7
8	generation_8
\.


--
-- Data for Name: legendaries; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.legendaries (id, name) FROM stdin;
1	non-legendary
2	legendary
\.


--
-- Data for Name: linking_table; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.linking_table (pokemon_id, type1_id, type2_id, ability1_id, ability2_id, ability3_id, egg_group1_id, egg_group2_id, legendary_id, specie_id, height, weight, catch_rate, normal_resist, fire_resist, water_resist, electric_resist, grass_resist, ice_resist, fighting_resist, poison_resist, ground_resist, flying_resist, psychic_resist, bug_resist, rock_resist, ghost_resist, dragon_resist, dark_resist, steel_resist, fairy_resist) FROM stdin;
0	1	2	1	2	0	1	2	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
0	1	2	1	2	0	1	2	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
\.


--
-- Data for Name: pokemon; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.pokemon (id, dex_num, name, hp, atk, spatk, def, spdef, spd) FROM stdin;
1	1	bulbasaur	45	49	49	65	65	45
\.


--
-- Data for Name: species; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.species (id, name) FROM stdin;
\.


--
-- Data for Name: types; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.types (id, name) FROM stdin;
1	none
2	grass
3	poison
\.


--
-- Name: abilities_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.abilities_id_seq', 3, true);


--
-- Name: egg_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.egg_groups_id_seq', 3, true);


--
-- Name: generations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.generations_id_seq', 8, true);


--
-- Name: legendaries_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.legendaries_id_seq', 2, true);


--
-- Name: pokemon_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.pokemon_id_seq', 1, true);


--
-- Name: species_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.species_id_seq', 1, false);


--
-- Name: types_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.types_id_seq', 3, true);


--
-- PostgreSQL database dump complete
--

