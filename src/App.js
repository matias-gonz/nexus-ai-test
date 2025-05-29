import Header from './components/Header';
import Resume from './components/Resume';
import Bio from './components/Bio';
import ContactForm from './components/ContactForm';
import Footer from './components/Footer';

function App() {
  return (
    <div className="App">
      <Header />
      <main>
        <Resume />
        <Bio />
        <ContactForm />
      </main>
      <Footer />
    </div>
  );
}

export default App;