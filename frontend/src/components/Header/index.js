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
        Existem n servidores numerados de 0 a n - 1 conectados por conexões servidor-servidor não direcionadas formando uma rede onde conexões[i] = [ai, bi] representa uma conexão entre servidores ai e bi. Qualquer servidor pode alcançar outros servidores direta ou indiretamente através da rede.
        Uma conexão crítica é uma conexão que, se removida, tornará alguns servidores incapazes de alcançar algum outro servidor.
        Retorna todas as conexões críticas na rede em qualquer ordem.
     </p>
  </header>
  );
}