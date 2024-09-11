import React, { useState } from 'react';
import { Camera } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';

const Signup = () => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [phone, setPhone] = useState('');
  const [age, setAge] = useState('');
  const [address, setAddress] = useState('');
  const [faceVerified, setFaceVerified] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (faceVerified) {
      console.log('Booking submitted:', { name, email, phone, age, address });
      // Here you would typically send the data to your backend
    } else {
      alert('Please verify your face before booking.');
    }
  };

  const verifyFace = () => {
    // This is where you'd integrate with a face recognition API
    // For this example, we'll just simulate a successful verification
    setTimeout(() => {
      setFaceVerified(true);
      alert('Face verified successfully!');
    }, 2000);
  };

  return (
    <Card className="w-full max-w-md mx-auto">
      <CardHeader>
        <CardTitle>Bus Ticket Registration</CardTitle>
      </CardHeader>
      <CardContent>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <Label htmlFor="name">Name</Label>
            <Input
              id="name"
              value={name}
              onChange={(e) => setName(e.target.value)}
              required
            />
          </div>
          <div>
            <Label htmlFor="email">Email</Label>
            <Input
              id="email"
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>
          <div>
            <Label htmlFor="phone">Phone Number</Label>
            <Input
              id="phone"
              type="tel"
              value={phone}
              onChange={(e) => setPhone(e.target.value)}
              required
            />
          </div>
          <div>
            <Label htmlFor="age">Age</Label>
            <Input
              id="age"
              type="number"
              value={age}
              onChange={(e) => setAge(e.target.value)}
              required
              min="0"
              max="120"
            />
          </div>
          <div>
            <Label htmlFor="address">Address</Label>
            <Input
              id="address"
              value={address}
              onChange={(e) => setAddress(e.target.value)}
              required
            />
          </div>
          <div>
            <Button
              type="button"
              onClick={verifyFace}
              className={`w-full ${faceVerified ? 'bg-green-500' : 'bg-blue-500'}`}
            >
              <Camera className="mr-2 h-4 w-4" />
              {faceVerified ? 'Face Verified' : 'Verify Face'}
            </Button>
          </div>
          <Button type="submit" className="w-full">
            Book Ticket
          </Button>
        </form>
      </CardContent>
    </Card>
  );
};

export default Signup;
