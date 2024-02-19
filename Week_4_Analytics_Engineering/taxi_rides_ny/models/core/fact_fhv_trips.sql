{{
    config(
        materialized='table'
    )
}}

with fhv_data as (
    select *,
        'fhv' as service_type
    from {{ ref('stg_fhv_tripdata') }}
),

dim_zones as (
    select * from {{ ref('dim_zones') }}
    where borough != 'Unknown'
)

SELECT
    fhv_data.dispatching_base_num,
    fhv_data.affiliated_base_number,
    fhv_data.sr_flag,
    fhv_data.pickup_datetime,
    fhv_data.dropoff_datetime,
    fhv_data.pickup_locationid,
    fhv_data.dropoff_locationid,
    fhv_data.service_type,

    pickup_zone.borough as pickup_borough,
    pickup_zone.zone as pickup_zone,

    dropoff_zone.borough as dropoff_borough,
    dropoff_zone.zone as dropoff_zone

FROM fhv_data
INNER JOIN dim_zones AS pickup_zone 
ON fhv_data.pickup_locationid = pickup_zone.locationid
INNER JOIN dim_zones AS dropoff_zone
ON fhv_data.dropoff_locationid = dropoff_zone.locationid