import "./App.css";
import DataTable from "datatables.net-react";
import DT from "datatables.net-dt";
import { useState } from "react";

DataTable.use(DT);

function App() {
  const [tableData] = useState([
    ["Tiger Nixon", "System Architect"],
    ["Garrett Winters", "Accountant"],
  ]);
  return (
    <>
      <div>
        <DataTable data={tableData} className="display">
          <thead>
            <tr>
              <th>Name</th>
              <th>Position</th>
            </tr>
          </thead>
        </DataTable>
      </div>
    </>
  );
}

export default App;
