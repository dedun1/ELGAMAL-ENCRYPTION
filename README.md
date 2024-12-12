Challenges Faced During Implementation And Findings:

1. Prime Number Generation: the problem is Generating a large random prime (p) was challenging, as smaller primes could compromise security, while larger primes increased computation time.
    Solution: Used sympy.isprime to validate prime numbers efficiently and opted for 8-bit primes for this demonstration. Larger primes can be used for enhanced security
   
2.Finding a Primitive Root: problem is Identifying a generator (g) for the multiplicative group mod p required computational effort, especially for small primes with limited primitive roots.
   Solution: Implemented an efficient search using modular arithmetic to check all potential generators.
   
3.Randomness in Encryption: Issue: Ensuring each encryption used a unique random value (k) to prevent patterns in the ciphertext.
   Solution: Generated a fresh random k for each character during encryption.
   
4- security depends on key size if the P is large it would be more secure but would increase computational time to process

5- randomness of k makes sure identical messages encrypt in different ciphertexts, makes the security stronger
