

select ord_id,ord_datetime,ord_an,round(((an_price - an_cost)::numeric/an_cost)*100,3) as markup from analysis as a 
join orders as o on
a.an_id = o.ord_an
