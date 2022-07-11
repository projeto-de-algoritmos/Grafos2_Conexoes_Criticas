import React from 'react';
import "./styles.css"
import network from "../../assets/network.png"

export default function Header() {
  return (
    <header className="header">
      <div className='inline-flex'>
        <img src={network} className="header-logo" alt="logo"/>
        <h1 className='header-h1'>Conexões críticas <br />em uma rede</h1>
      </div>
      <p className='header-p'>
        Uma conexão crítica é uma conexão que, se removida, tornará alguns servidores incapazes de alcançar algum outro servidor.
        Retorna todas as conexões críticas na rede em qualquer ordem. Este algorimo é um exemplo de como esta conexão funciona!
        <br/>
        <br/>
        <b>Regras:</b>
        <br/>
        <br/>
        <b>1-</b> Um nó não pode se conectar a ele mesmo.
        <br/>
        <b>2-</b> Todo nó tem que se conectar pelo menos uma vez.
        <br/>
        <b>3-</b> Insira uma conexão por linha, igual ao exemplo abaixo.
     </p>
  </header>
  );
}