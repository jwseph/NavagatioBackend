import { React, Fragment, useEffect, useState } from 'react';
const TripList = () => {
    const [data, setData] = useState([{}])

    useEffect(() => {
      fetch("/trips").then(
        res => res.json()
      ).then(
        data => {
          setData(data)
          console.log(data);
        }
      )
    }, [])

    return(
        <Fragment>
            {(typeof data.top_trips === 'undefined') ? (
                <Fragment>
                    <p>Loading...</p>
                    <img src="images/loading.png" className='loading'/>
                </Fragment>
            ): (
                <ul>
                {
                    data.top_trips.map((trip , i) => (
                    <li key={i}>{trip}</li>
                    ))
                }
                </ul>
            )}
        </Fragment>
    )
}

export default TripList