SELECT
    conname,
    pg_get_constraintdef(oid) AS definicao
FROM pg_constraint
WHERE conrelid = 'public.documento'::regclass
ORDER BY conname;