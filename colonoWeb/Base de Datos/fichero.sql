--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.5
-- Dumped by pg_dump version 9.5.5

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
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: colono14
--

CREATE TABLE django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE django_migrations OWNER TO colono14;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: colono14
--

CREATE SEQUENCE django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_migrations_id_seq OWNER TO colono14;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: colono14
--

ALTER SEQUENCE django_migrations_id_seq OWNED BY django_migrations.id;


--
-- Name: paginas_tc_patron; Type: TABLE; Schema: public; Owner: colono14
--

CREATE TABLE paginas_tc_patron (
    idpatron integer NOT NULL,
    xp integer,
    yp integer,
    contadorp integer NOT NULL
);


ALTER TABLE paginas_tc_patron OWNER TO colono14;

--
-- Name: paginas_tc_patron_idpatron_seq; Type: SEQUENCE; Schema: public; Owner: colono14
--

CREATE SEQUENCE paginas_tc_patron_idpatron_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE paginas_tc_patron_idpatron_seq OWNER TO colono14;

--
-- Name: paginas_tc_patron_idpatron_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: colono14
--

ALTER SEQUENCE paginas_tc_patron_idpatron_seq OWNED BY paginas_tc_patron.idpatron;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: colono14
--

ALTER TABLE ONLY django_migrations ALTER COLUMN id SET DEFAULT nextval('django_migrations_id_seq'::regclass);


--
-- Name: idpatron; Type: DEFAULT; Schema: public; Owner: colono14
--

ALTER TABLE ONLY paginas_tc_patron ALTER COLUMN idpatron SET DEFAULT nextval('paginas_tc_patron_idpatron_seq'::regclass);


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: colono14
--


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: colono14
--

SELECT pg_catalog.setval('django_migrations_id_seq', 1, true);


--
-- Data for Name: paginas_tc_patron; Type: TABLE DATA; Schema: public; Owner: colono14
--



--
-- Name: paginas_tc_patron_idpatron_seq; Type: SEQUENCE SET; Schema: public; Owner: colono14
--

SELECT pg_catalog.setval('paginas_tc_patron_idpatron_seq', 1, false);


--
-- Name: django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: colono14
--

ALTER TABLE ONLY django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: paginas_tc_patron_pkey; Type: CONSTRAINT; Schema: public; Owner: colono14
--

ALTER TABLE ONLY paginas_tc_patron
    ADD CONSTRAINT paginas_tc_patron_pkey PRIMARY KEY (idpatron);


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
create or replace function filtrarPatrones(limite float)
returns boolean as 
$BODY$
declare
	cursor_primario refcursor;
	cursor_secundario refcursor;
	
	id_p integer;
	x integer;
	y integer;
	contador_p integer;
	
	
	id_s integer;
	contador_s integer;
	
begin
	open cursor_primario for select idpatron,xp,yp,contadorp from paginas_tc_patron;
	loop
		fetch cursor_primario into id_p,x,y,contador_p;
		exit when not FOUND;
		open cursor_secundario for select idpatron,contadorp from paginas_tc_patron where idpatron<>id_p and @(|/(((x-paginas_tc_patron.xp)^2)+((y-paginas_tc_patron.yp)^2)))<=limite; 
		loop
		fetch cursor_secundario into id_s,contador_s;
		exit when not FOUND;
			if contador_p>contador_s then
				UPDATE paginas_tc_patron
				SET contadorp=contadorp+contador_s
				WHERE idpatron = id_p;

				delete from paginas_tc_patron where idpatron=id_s; 
			else
				UPDATE paginas_tc_patron
				SET contadorp=contadorp+contador_p
				WHERE idpatron = id_s;

				delete from paginas_tc_patron where idpatron=id_p; 
				
			end if;
		end loop;	
		close cursor_secundario;
		
	end loop;
	close cursor_primario;
	return true;
end;
$BODY$
language plpgsql;

create or replace function filtrarRuido(limite integer)
returns boolean as 
$BODY$
begin
	delete from paginas_tc_patron where contadorp<=limite;
	return true;
end;
$BODY$
language plpgsql;

