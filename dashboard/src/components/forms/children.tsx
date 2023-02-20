import { useContext } from "react";
import { HouseholdContext } from "../../contexts/HouseholdContext";
import { Birthday } from "./attributes/Birthday";
import { PhysicalDisability } from "./attributes/PhysicalDisability";
import { MentalDisability } from "./attributes/MentalDisability";
import { IntellectualDisability } from "./attributes/IntellectualDisability";

export const FormChildren = () => {
  const { household, setHousehold } = useContext(HouseholdContext);
  return (
    <>
      {household.世帯.世帯1.児童一覧 &&
        household.世帯.世帯1.児童一覧.map(
          (childName: string, index: number) => (
            <div key={index}>
              <h3>{index + 1}人目の子ども</h3>
              <Birthday personName={childName} />
              <PhysicalDisability personName={childName} />
              <MentalDisability personName={childName} />
              <IntellectualDisability personName={childName} />
              <br></br>
            </div>
          )
        )}
    </>
  );
};
