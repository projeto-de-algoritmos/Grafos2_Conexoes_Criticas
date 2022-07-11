import { generateGraph } from '../../service/api';
import React, { useEffect, useState } from "react";
import { useForm } from "react-hook-form"
import "./styles.css"

export default function Board() {
  const { register, control } = useForm()
  const [img, setImg] = useState(null);

  const generateGraphs = async (data) => {
    // const sendObj = {
    //   nodes_number: 4,
    //   edges: [[0,1],[1,2],[2,0],[1,3]]
    // }
    // try {
    //   console.log("RODEI");
    //   const graph = await generateGraph(sendObj)
    //   console.log(graph);
    //   setImg(graph.data)
    // } catch (error) {
      
    // }
    console.log(data.nos);
  }

  const handleSubmit = () => {
    var input = document.querySelector("#nos");
    var texto = input.value;
    console.log(texto);
    var input2 = document.querySelector("#conexoes");
    var texto2 = input2.value;
    console.log(texto2);
  }

  return (
    <div className='board'>
          <div>
            <div className='board-span-input'>
              <span className='board-span'>Número de nós:</span>
              <input id="nos" className='board-input-1' max="2"
              />
            </div>
            <div className='board-span-input'>
              <span className='board-span'>Conexões:</span>
              <textarea id="conexoes" className='board-text-area' cols="2"></textarea>
            </div>
          </div>
        <button onClick={handleSubmit} type='submit' className='board-button'>Gerar conexões!</button>
    </div>
  );
}