--DO NOT MODIFY THIS FILE, IT IS GENERATED AUTOMATICALLY FROM SOURCES
-- Complain if script is sourced in psql, rather than via CREATE EXTENSION
\echo Use "ALTER EXTENSION cdb_dataservices_client UPDATE TO '0.24.0'" to load this file. \quit

-- Make sure we have a sane search path to create/update the extension
SET search_path = "$user",cartodb,public,cdb_dataservices_client;

-- HERE goes your code to upgrade/downgrade
ALTER TYPE cdb_dataservices_client.obs_meta_timespan ADD ATTRIBUTE timespan_alias text;
ALTER TYPE cdb_dataservices_client.obs_meta_timespan ADD ATTRIBUTE timespan_range datarange;