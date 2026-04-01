From token_logrel Require Import temp2.

Notation "|===> Q" := (let _ := token_world in Q) (at level 99).

Section tupd_proofs.
  Lemma tupd_intro P : P -> |===> P.
  Proof.  Admitted.
End tupd_proofs.


(* this works *)

From Stdlib.QArith Require Import Qcanon.

Notation "|===> Q" := (let _ := Qc in Q) (at level 99).

Section tupd_proofs.
  Lemma tupd_intro_Qc P : P -> |===> P.
  Proof.  Admitted.
End tupd_proofs.
