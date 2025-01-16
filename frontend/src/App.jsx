import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import Sidebar from "./components/Sidebar.jsx";
import Header from "./components/Header.jsx";
import Sites from "./pages/Sites.jsx";
import Plans from "./pages/Plans.jsx";
import News from "./pages/News.jsx";
import Quotes from "./pages/Quotes.jsx";
import Achievement from "./pages/Achievement.jsx";
import Video from "./pages/Video.jsx";


const queryClient = new QueryClient();

const App = () => {
  return (
    <QueryClientProvider client={queryClient}>
    <Router>
      <div className="flex">
        <Sidebar />
        <div className="flex-1">
          <Header />
          <div className="p-4 mt-[64px] ml-[200px]">
            <Routes>
              <Route path="/" element={<Sites />} />
              <Route path="/plans" element={<Plans />} />
              <Route path="/news" element={<News />} />
              <Route path="/Quotes" element={<Quotes />} />
              <Route path="/Achievement" element={<Achievement />} />
              <Route path="/Video" element={<Video />} />
            </Routes>
          </div>
        </div>
      </div>
    </Router>
    </QueryClientProvider>
  );
};

export default App;