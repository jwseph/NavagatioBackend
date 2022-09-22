import { React, useEffect, useState } from 'react';
import styles from './SearchBar.module.css';
function SearchBar() {
    const [search_query, setSearch_query] = useState('')
    const [places, setPlaces] = useState([])
    

    useEffect(() => {
      fetch(`/search/${search_query}`).then(
        res => res.json()
      ).then(
        places_data => {
          setPlaces(places_data.results)
        }
      )
    }, [search_query])

    console.log(places);

    return(
      <div>
        <input className={styles.search_bar} type="text" placeholder='Where To?' 
          onChange={(e)=>setSearch_query(
            e.currentTarget.value.charAt(0).toUpperCase() + 
            e.currentTarget.value.slice(1))}/>
        <ul>
          {
            places.map((place, i)=> {
              return(<li style={{listStyle:"none"}} key={i}>{place.city}, {place.country}</li>)
            })
          }
        </ul>
      </div>
    )
}

export default SearchBar