create table parents as
  select 'ace' as parent, 'bella' as child union
  select 'ace'          , 'charlie'        union
  select 'daisy'        , 'hank'           union
  select 'finn'         , 'ace'            union
  select 'finn'         , 'daisy'          union
  select 'finn'         , 'ginger'         union
  select 'ellie'        , 'finn';

create table dogs as
  select 'ace' as name, 'long' as fur, 26 as height union
  select 'bella'      , 'short'      , 52           union
  select 'charlie'    , 'long'       , 47           union
  select 'daisy'      , 'long'       , 46           union
  select 'ellie'      , 'short'      , 35           union
  select 'finn'       , 'curly'      , 32           union
  select 'ginger'     , 'short'      , 28           union
  select 'hank'       , 'curly'      , 31;

create table sizes as
  select 'toy' as size, 24 as min, 28 as max union
  select 'mini'       , 28       , 35        union
  select 'medium'     , 35       , 45        union
  select 'standard'   , 45       , 60;


-- All dogs with parents ordered by decreasing height of their parent
create table by_parent_height as
  select child from parents, dogs where parent = name order by height DESC;


-- The size of each dog
create table size_of_dogs as
  select dogs.name, sizes.size from dogs, sizes where dogs.height <= sizes.max and dogs.height > sizes.min;


-- [Optional] Filling out this helper table is recommended
create table siblings as
  select a.child || ' and ' || b.child as name, c.size as first_size, d.size as second_size 
    from parents as a, parents as b, size_of_dogs as c, size_of_dogs as d
    where a.parent = b.parent and a.child <> b.child and a.child < b.child
          and c.name = a.child and d.name = b.child;

-- Sentences about siblings that are the same size
create table sentences as
  select 'The two siblings, ' || name || ', have the same size: ' || first_size 
    from siblings 
    where first_size = second_size; 


-- -- Height range for each fur type where all of the heights differ by no more than 30% from the average height
-- create table low_variance as
--   select 'REPLACE THIS LINE WITH YOUR SOLUTION';

