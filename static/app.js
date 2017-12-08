class App extends React.Component{

	state = {
		client: {
			name:'',
			email:''
		}, 
		response:null
	};

	onChange = (e) => {
		const value = e.target.value;
		const field = e.target.name;
		let {client} = this.state;
		client[field] = value;
		this.setState({client});
	};

	submitClient = (e) => {
		e.preventDefault();
		//console.log(this.state.client);
		const body = JSON.stringify(this.state.client);
		const req = {
			method:"POST",
			body:body,
			headers:{
				"Content-Type":"application/json"
			}
		}
		fetch("/send_mail/", req)
			.then(r=>{
				if(!r.ok) throw r;
				return r;
			})
			.then(response=>{
				this.setState({response});
			})
			.catch(e=>{
				console.log(e);
				alert("No pudimos registrarte, intentalo de nuevo" + e.statusText);
			});
	};

	render(){
		if(this.state.response) return <div className="subscribe"><h3>¡Gracias!</h3><h5>Revisa tu correo ;)</h5></div>
		return(
				<div className="subscribe">
					<h3>¿Te gustó este articulo?</h3>
					<h5>¡Registrate a nuestro newsLetter!</h5>
					<form onSubmit={this.submitClient} validated>
						<input onChange={this.onChange} required type="text" name="name" placeholder="Nombre" />
						<input onChange={this.onChange} required type="email" name="email" placeholder="Correo electrónico"/>
						<input type="submit" value="¡Si Quiero!" />	
					</form>	
				</div>
			);
	}
}

ReactDOM.render(<App/>, root);