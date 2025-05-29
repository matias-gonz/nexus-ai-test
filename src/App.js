import Resume from './components/Resume';
import Bio from './components/Bio';
import ContactForm from './components/ContactForm';

function App() {
  return (
    <div className="App">
      <header className="bg-gray-100 py-4">
        <h1 className="text-center text-2xl font-bold">My Personal Website</h1>
      </header>
      <main>
        <Resume />
        <Bio />
        <ContactForm />
      </main>
      <footer className="bg-gray-100 py-4 text-center">
        <p>&copy; 2024 My Website</p>
      </footer>
    </div>
  );
}

export default App;