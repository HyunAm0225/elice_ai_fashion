import { useMediaQuery } from "react-responsive";

const Mobile = ({ children }) => {
  const isMobile = useMediaQuery({ maxWidth: "767.9px" });
  return isMobile ? children : null;
};

const Tablet = ({ children }) => {
  const isTablet = useMediaQuery({
    minWidth: "768px",
    maxWidth: "1023.9px",
  });
  return isTablet ? children : null;
};

const PC = ({ children }) => {
  const isPC = useMediaQuery({
    minWidth: "1024px",
    maxWidth: "1279.9px",
  });
  return isPC ? children : null;
};

const PCwide = ({ children }) => {
  const isPCwide = useMediaQuery({ minWidth: "1280px" });
  return isPCwide ? children : null;
};

export { Mobile, Tablet, PC, PCwide };
