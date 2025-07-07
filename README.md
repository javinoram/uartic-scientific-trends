# uartic-scientific-trends
Python codes to recreate some results of https://zenodo.org/records/15683128

This is done to recreate values from Chile, using partial counting.

## Filter used in the work:
```
( TITLE-ABS-KEY ( "antarc*" ) AND NOT TITLE-ABS-KEY ( "candida" OR "except antarctica" OR "not antarctica" OR "other than Antarctica" ) ) OR TITLE-ABS-KEY ( "transantarctic" OR "ross sea" OR "amundsen sea" OR "weddell sea" OR "southern ocean" ) AND ( LIMIT-TO ( AFFILCOUNTRY , "Chile" ) ) AND ( LIMIT-TO ( PUBYEAR , 2022 ) OR LIMIT-TO ( PUBYEAR , 2023 ) OR LIMIT-TO ( PUBYEAR , 2024 ) )
``` 


## Filter used by INACH (originally create for WOS and adjusted using chatgpt):
``` 
TITLE-ABS-KEY ( antarct* ) AND NOT TITLE-ABS-KEY ( durvillaea OR candida OR "except antarctica" OR "not antarctica" OR "nothofagus antarctica" ) AND ( LIMIT-TO ( AFFILCOUNTRY , "Chile" ) ) AND ( LIMIT-TO ( PUBYEAR , 2022 ) OR LIMIT-TO ( PUBYEAR , 2023 ) OR LIMIT-TO ( PUBYEAR , 2024 ) )
```

It is well known that the values used by this filter have some subantartic papers. This filter is used in ILAIA magazine (by INACH), but is manually treated to eliminate not antarctic papers. So, ILAIA values are less that the one shows using this filter.


## Preliminar results

