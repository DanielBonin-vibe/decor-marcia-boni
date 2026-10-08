SELECT
    column_name,
    character_maximum_length
FROM information_schema.columns
WHERE table_name = 'cliente'
AND column_name = 'estado';