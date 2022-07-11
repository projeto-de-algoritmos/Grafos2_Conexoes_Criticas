import './App.css';
import React, { useEffect, useState } from "react";
import { generateGraph } from './service/api';

function App() {

  const [img, setImg] = useState(null);

  // useEffect (() => {
  //   console.log(img);
  // }, [img])

  // const fetchImage = async (data) => {
  //   const res = await fetch(data);
  //   const imageBlob = await res.blob();
  //   const imageObjectURL = URL.createObjectURL(imageBlob);
  //   setImg(imageObjectURL);
  // };

  const generateGraphs = async () => {
    const sendObj = {
      nodes_number: 4,
      edges: [[0,1],[1,2],[2,0],[1,3]]
    }
    try {
      console.log("RODEI");
      const graph = await generateGraph(sendObj)
      console.log(graph);
    } catch (error) {
      
    }
  }

  return (
    <div className="App">
      <header className="App-header">
        <button onClick={generateGraphs}>
          Gerar grafos!
        </button>
        {img !== null &&
        <img src={img} className="App-logo" alt="logo" />  
        }

        <p>
        Existem n servidores numerados de 0 a n - 1 conectados por conexões servidor-servidor não direcionadas formando uma rede onde conexões[i] = [ai, bi] representa uma conexão entre servidores ai e bi. Qualquer servidor pode alcançar outros servidores direta ou indiretamente através da rede.
        Uma conexão crítica é uma conexão que, se removida, tornará alguns servidores incapazes de alcançar algum outro servidor.
        Retorna todas as conexões críticas na rede em qualquer ordem.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Olá mundo! Muda ao vivo! Brabo demais!
        </a>
      </header>
    </div>
  );
}

export default App;
