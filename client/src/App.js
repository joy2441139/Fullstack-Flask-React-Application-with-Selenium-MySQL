import { useEffect, useState } from "react";
import React from "react";
import "./App.css";

function App() {

  const [data, setData] = useState([{}])

  useEffect(() => {
    console.log("i fire once");
    fetch("/data").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        // console.log(data);
      }
    )
  }, [])
  return (
    <div className="app-container">
      {(typeof data.DBResult === 'undefined') ? (
        <p>loading...</p>
      ) : (
        <table>
          <thead>
            <tr>
              {data.DBResult[0].map((thead) => (
                <th>{thead}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {data.DBResult.slice(1).map((tbody, i) => (
              <tr>
                <td>{tbody[0]}</td>
                <td>{tbody[1]}</td>
                <td>{tbody[2]}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )
      }
    </div >
  )
}

export default App