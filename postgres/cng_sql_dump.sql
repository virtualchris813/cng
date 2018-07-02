--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.6
-- Dumped by pg_dump version 9.5.6

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: cng; Type: DATABASE; Schema: -; Owner: cng
--

CREATE DATABASE cng WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';


ALTER DATABASE cng OWNER TO cng;

\connect cng

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: hostname; Type: TABLE; Schema: public; Owner: cng
--

CREATE TABLE hostname (
    id integer NOT NULL,
    basename character varying(60) NOT NULL,
    incrementor character varying(10) NOT NULL,
    inc_width integer NOT NULL,
    fullname character varying(100) NOT NULL
);


ALTER TABLE hostname OWNER TO cng;

--
-- Name: hostname_id_seq; Type: SEQUENCE; Schema: public; Owner: cng
--

CREATE SEQUENCE hostname_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE hostname_id_seq OWNER TO cng;

--
-- Name: hostname_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cng
--

ALTER SEQUENCE hostname_id_seq OWNED BY hostname.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: cng
--

ALTER TABLE ONLY hostname ALTER COLUMN id SET DEFAULT nextval('hostname_id_seq'::regclass);


--
-- Data for Name: hostname; Type: TABLE DATA; Schema: public; Owner: cng
--

COPY hostname (id, basename, incrementor, inc_width, fullname) FROM stdin;
124	labvmtest-	1	6	labvmtest-000001
\.


--
-- Name: hostname_id_seq; Type: SEQUENCE SET; Schema: public; Owner: cng
--

SELECT pg_catalog.setval('hostname_id_seq', 124, true);


--
-- Name: basename_and_incrementor; Type: INDEX; Schema: public; Owner: cng
--

CREATE INDEX basename_and_incrementor ON hostname USING btree (basename, incrementor);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

