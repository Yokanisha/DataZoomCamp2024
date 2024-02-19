{{
    config(
        materialized='table'
    )
}}

with fact_trips_data as (
    select * from {{ ref('fact_trips') }}
),

fact_fhv_trips_data as (
    select * from {{ ref('fact_fhv_trips') }}
),

fact_unioned as (
select 
    service_type,
    pickup_datetime, 
    dropoff_datetime, 
    pickup_locationid, 
    dropoff_locationid,
    pickup_borough,
    pickup_zone,
    dropoff_borough,
    dropoff_zone
from fact_trips_data

union all

select 
    service_type,
    pickup_datetime, 
    dropoff_datetime, 
    pickup_locationid, 
    dropoff_locationid,
    pickup_borough,
    pickup_zone,
    dropoff_borough,
    dropoff_zone
from fact_fhv_trips_data
)

select * from fact_unioned