import { generateGraph } from '../../service/api';
import React, { useEffect, useState } from "react";
import { useForm } from "react-hook-form"
import "./styles.css"

export default function Board() {
  const [img, setImg] = useState(null);

  const generateGraphs = async (data) => {
    try {
      console.log("RODEI");
      const graph = await generateGraph(data)
      console.log(graph);
      setImg(graph.data.image_string)
    } catch (error) {
      alert("Não foi possível gerar as conexões, verifique se preencheu corretamente!")
    }
  }

  const handleSubmit = () => {
    try {    
      var input = document.querySelector("#nos");
      var number = input.value;
      var input2 = document.querySelector("#conexoes");
      var texto2 = input2.value;
      const res = texto2.split("\n");
      let arr = []
      console.log(res);
      for (let i of res){
        i = String(i);
        console.log(i);
        let split = i.split(",")
        if (split[0] === split[1] || (split[0] > number-1) || (split[1] > number-1)){
          throw new Error({ code : 403, message : "Exception" });
        }
        else 
          arr.push([ parseInt(split[0]), parseInt(split[1]) ])
      }
  
      const sendObj = {
        nodes_number: number,
        edges: arr
      }
      generateGraphs(sendObj)
    } catch (error) {
      alert("Não foi possível gerar as conexões, verifique se preencheu corretamente!")
    }
  }

  const onReset = () => {
    setImg(null)
  }

  return (
    <div className='board'>
          {img ? 
          <>
            <img src={`data:image/png;base64,` + img} alt="conexoes"/>
            <button onClick={onReset} className='board-button-2'>Tentar novamente!</button>
          </>
          :
            <div>
              <div className='board-span-input'>
                <span className='board-span'>Número de nós:</span>
                <input id="nos" className='board-input-1' max="2" placeholder='4'
                />
              </div>
              <div className='board-span-input'>
                <span className='board-span'>Conexões:</span>
                <textarea id="conexoes" className='board-text-area' cols="2" placeholder="0,1&#10;1,2&#10;2,0&#10;1,3"></textarea>
              </div>
            <button onClick={handleSubmit} type='submit' className='board-button'>Gerar conexões!</button>
            </div>
          }
    </div>
  );
}