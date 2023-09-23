SELECT t1.login, count(*)
FROM "Couriers" t1
JOIN "Orders" t2 on t2."courierId" = t1.id
WHERE t2."inDelivery"=TRUE
GROUP BY t1.login;

SELECT
    track,
    CASE
        WHEN finished is TRUE THEN 2
        WHEN cancelled is TRUE THEN -1
        WHEN "inDelivery" is TRUE THEN 1
        ELSE 0
    END as status
FROM "Orders";